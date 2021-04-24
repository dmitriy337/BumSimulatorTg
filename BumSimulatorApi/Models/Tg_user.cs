using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BumSimulatorApi.Models
{
    public class Tg_user
    {
        public long Id { get; set; }
        public string Username { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public DateTime Date { get; set; }

        public Character character => new Character {dateTime = new DateTime(2010, 07, 28),
        happy_level=100,
        eat_level = 100,
        health_level = 100,
        bottles = 10,
        TrackDay = new DateTime(2010, 07, 28),
        status = UserRole.Bum,
        money=500,
        rating=0
        };
    }
}
