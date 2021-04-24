using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BumSimulatorApi.Models
{
    public class Health
    {
        public long Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public int Price { get; set; }
        public int HowMuchHealth { get; set; }
        public int HowMuchEat { get; set; }
        public int HowMuchDrink { get; set; }
    }
}
