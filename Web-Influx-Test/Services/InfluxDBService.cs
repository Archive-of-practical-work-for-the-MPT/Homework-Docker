using InfluxDB.Client;
using Web_Influx_Test.Models;
using InfluxDB.Client.Api.Domain;

namespace Web_Influx_Test.Services
{
    public class InfluxDBService : IDisposable
    {
        private readonly InfluxDBClient _client;
        private const string bucket = "metrics";
        private const string org = "MPT";
        private readonly Random _random = new Random();
        private readonly Timer _timer;

        public InfluxDBService()
        {
            var token = "_pOGra7II5cypxk5XxWvOwLHDjSlADOwAGXKRPJzsKgtJcvvhNyMIkHZDRiVel4ACX-IU5C3PF2W4IhwdmXPTQ==";
            _client = new InfluxDBClient("http://localhost:8086", token);
            _timer = new Timer(SendMetric, null, TimeSpan.Zero, TimeSpan.FromSeconds(15));

        }

        private void SendMetric(object? state)
        {
            try
            {
                var randomValue = _random.NextDouble() * 100;
                var number_counter = new NumberCounter
                {
                    Host = "localhost",
                    UsedPercent = randomValue,
                    Time = DateTime.UtcNow
                };

                WriteMeasurement(number_counter);
            }
            catch { 
            }
        }

        public void WriteMeasurement<T>(T measurement) where T : class
        {
            using (var writeApi = _client.GetWriteApi())
            {
                writeApi.WriteMeasurement(measurement, WritePrecision.Ns, bucket, org);
            }
        }

        public void Dispose()
        {
            _timer.Dispose();
            _client.Dispose();
        }

    }
}
