using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;
using System.Linq;
using System.Threading.Tasks;

namespace BumSimulatorApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class AllUsersController : ControllerBase
    {
        Models.AppContext db;
        public AllUsersController(Models.AppContext context)
        {
            db = context;
            
        }

        [HttpGet]
        public async Task<ActionResult<IEnumerable<Models.Tg_user>>> Get()
        {
            return await db.Tg_users.Include(x => x.character).ToListAsync();
        }

    }
}
