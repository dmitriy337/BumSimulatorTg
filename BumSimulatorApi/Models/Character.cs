using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BumSimulatorApi.Models
{
    public class Character
    {
        public long Id { get; set; }
        public DateTime dateTime { get; set; }
        public DateTime TrackDay { get; set; }
        public int age => this.dateTime.Year;
        public long money { get; set; }
        public long bottles { get; set; }
        public long rating { get; set; }
        public UserRole status { get; set; }
        public int happy_level { get; set; }
        public int eat_level { get; set; }
        public int health_level { get; set; }
    }

    public enum UserRole
    {
        Bum,
        Robber,
        Poor
    }
}
