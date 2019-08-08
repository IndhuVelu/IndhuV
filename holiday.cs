using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Rextester
{
    public class Program
    {
        public static void Main(string[] args)
        {
           
            string day;
            day=Console.ReadLine();
            if(day=="Saturday" || day=="Sunday")
            {
                Console.WriteLine("yes");
                
            }
            else
            {
                Console.WriteLine("no");
            }
        }
    }
}
