using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Player
{
    static void Main(string[] args)
    {
        string[] inputs;
        inputs = Console.ReadLine().Split(' ');
        int W = int.Parse(inputs[0]); // width of the building.
        int H = int.Parse(inputs[1]); // height of the building.
        int N = int.Parse(Console.ReadLine()); // maximum number of turns before game over.
        inputs = Console.ReadLine().Split(' ');
        int X0 = int.Parse(inputs[0]);
        int Y0 = int.Parse(inputs[1]);

        // game loop
        while (true)
        {
            string BOMB_DIR = Console.ReadLine(); // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

            // Write an action using Console.WriteLine()
            // To debug: Console.Error.WriteLine("Debug messages...");

            int verticalMovement = 0;
            int horizontalMovement = 0;
            switch(BOMB_DIR)
            {
                case "U":
                    verticalMovement = 1;
                    break;
                case "UR":
                    verticalMovement = 1;
                    horizontalMovement = 1;
                    break;
                case "R":
                    horizontalMovement = 1;
                    break;
                case "DR":
                    verticalMovement = -1;
                    horizontalMovement = 1;
                    break;
                case "D":
                    verticalMovement = -1;
                    break;
                case "DL":
                    verticalMovement = -1;
                    horizontalMovement = -1;
                    break;
                case "L":
                    horizontalMovement = -1;
                    break;
                case "UL":
                    verticalMovement = 1;
                    horizontalMovement = -1;
                    break;
                default:
                    horizontalMovement = 0;
                    verticalMovement = 0;
                    break;
            }

            X0 += horizontalMovement;
            Y0 -= verticalMovement;

            Console.WriteLine(X0.ToString() + " " + Y0.ToString()); // the location of the next window Batman should jump to.
        }
    }
}