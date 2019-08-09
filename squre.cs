
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
            //Your code goes here
            int n,temp,sum=0,r;
            n=int.Parse(Console.ReadLine());
            temp=n;
            while(n!=0)
            {
                r=n%10;
                sum=sum+(r*r);
                n=n/10;
            }
            Console.WriteLine(sum);
        }
    }
}
