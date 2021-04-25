using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;

namespace BumSimulatorApi.Models
{
    public class Character
    {
        [System.ComponentModel.DataAnnotations.Key]
        public long Id { get; set; }
        public DateTime dateTime { get; set; } 
        public DateTime TrackDay { get; set; }
        public int age { get; set; }
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
