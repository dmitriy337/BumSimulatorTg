using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BumSimulatorApi.Models
{
    public class Character
    {
        public long Id { get; set; }
        public int age { get; set; }
        public long money { get; set; }
        public long bottles { get; set; }
        public long rating { get; set; }
        public UserRole status { get; set; }

    }

    public enum UserRole
    {
        Bum,
        User
    }
}
