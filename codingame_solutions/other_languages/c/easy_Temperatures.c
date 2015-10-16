#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
int main()
{
    int N; // the number of temperatures to analyse
    scanf("%d", &N); fgetc(stdin);
    char TEMPS[256]; // the N temperatures expressed as integers ranging from -273 to 5526
    fgets(TEMPS,256,stdin); // the N temperatures expressed as integers ranging from -273 to 5526
    
    int closestTemperature = 9999;
    int closestDifference = 9999;
    int numberOfTempsProcessed = 0;
    int currentIndex = 0;
    while(numberOfTempsProcessed < N)
    {
        int flagMinus = 0;
        int currentValue = 0;
        int currentMultiplier = 10;
        int flagWholeValue = 0;
        while(!flagWholeValue)
        {
            char currentSign = TEMPS[currentIndex];
            if(currentSign == '-')
            {
                flagMinus = 1;
            }
            else if(currentSign >= '0' && currentSign <= '9')
            {
                int signAsIntValue = (int)(currentSign - '0');
                currentValue = signAsIntValue + currentMultiplier*currentValue;
            }
            else
            {
                if(flagMinus)
                {
                    currentValue *= -1;
                }
                flagWholeValue = 1;
            }
            currentIndex++;
        }
        
        int difference = abs(currentValue);
        fprintf(stderr, "value: %d\n", currentValue);
        
        if(difference < closestDifference)
        {
            closestDifference = difference;
            closestTemperature = currentValue;
        }
        else if(difference == closestDifference)
        {
            fprintf(stderr, "closestDifference: %d\n", closestDifference);
            fprintf(stderr, "closestTemperature: %d\n", closestTemperature);
            fprintf(stderr, "difference: %d\n", difference);
            fprintf(stderr, "temperature: %d\n", currentValue);
            if(currentValue > closestTemperature)
            {
                closestDifference = difference;
                closestTemperature = currentValue;
            }
        }

        numberOfTempsProcessed++;
    }
    
    fprintf(stderr, "closestDifference: %d\n", closestDifference);
    fprintf(stderr, "closestTemperature: %d\n", closestTemperature);

    // Write an action using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    if(N==0)
    {
        printf("0\n");
    }
    else
    {
        printf("%d\n", closestTemperature);
    }
}