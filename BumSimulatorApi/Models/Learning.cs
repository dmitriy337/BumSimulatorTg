using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BumSimulatorApi.Models
{
    public class Learning
    {
        public long Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public int Price { get; set; }
        public int HowMuchRating { get; set; }
        public int UnlockRating { get; set; }
    }
}
