#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
int main()
{
    int fire;
    int new_course = 0;

    // game loop
    while (1) {
        int SX;
        int SY;
        int highest = 0;
        int highest_no = 0;
        cin >> SX >> SY; cin.ignore();
        if (new_course != SY) fire = 0;
        new_course = SY;
        for (int i = 0; i < 8; i++) {
            int MH; // represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
            cin >> MH; cin.ignore();
            if (MH > highest) {
                highest_no = i;
                highest = MH;
            }
        }
        if ((SX == highest_no) and (fire == 0)) {
            fire = 1;
            cout << "FIRE" << endl;
        }
        

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;

       else cout << "HOLD" << endl; // either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).
        
    }
}