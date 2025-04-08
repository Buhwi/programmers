#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    bool answer = true;
    int temp = 0;
    int n = x;
    
    while (n > 0)
    {
        temp += n % 10;
        n = n / 10;
    }
    if (x % temp != 0)
    {
        return false;
    }
    
    return answer;
}