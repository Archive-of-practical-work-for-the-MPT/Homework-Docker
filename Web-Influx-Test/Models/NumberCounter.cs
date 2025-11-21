using InfluxDB.Client.Core;

namespace Web_Influx_Test.Models
{
    [Measurement("number_counter")]
    public class NumberCounter
    {
        [Column("host", IsTag = true)] public string Host { get; set; }
        [Column("used_percent")] public double? UsedPercent { get; set; }
        [Column(IsTimestamp = true)] public DateTime Time { get; set; }
    }
}
