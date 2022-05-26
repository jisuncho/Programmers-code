#include <string>
#include <vector>
#include <deque>
#include <numeric>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    vector<int> v(bridge_length, 0);
    int sum = 0;
    int i = 0;
    while(1){
        sum = accumulate(v.begin(), v.end(), 0);
        if(sum + truck_weights[i] <= weight){
            v.push_back(truck_weights[i++]);
            v.erase(v.begin());
        }
        else{
            v.push_back(0);
            v.erase(v.begin());
        }
        answer++;
        sum = accumulate(v.begin(), v.end(), 0);
        if(sum == 0 && i >= truck_weights.size())
            break;
    }
    return answer;
}