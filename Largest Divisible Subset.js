/**
 * @param {number[]} nums
 * @return {number[]}
 */

var largestDivisibleSubset = function(nums) {
    var ans = [];
    var prev = [];
    var len = nums.length;
    if (!len){
        return [];
    }
    for (var i = 0 ; i < len ; i ++){
        ans[i] = 1;
        prev[i] = -1;
    }
    nums.sort(function(a,b){return a-b;});
    var maxValue = 1;
    var idx = 0;
    for (var i = 1 ; i < len ; i ++){
        for (var j = 0 ; j < i ; j ++){
            if (nums[i] % nums[j] === 0){
                if (ans[j] + 1 > ans[i]){
                    prev[i] = j;
                    ans[i] = ans[j] + 1;
                }
            }
        }
        if (maxValue < ans[i]){
            maxValue = ans[i];
            idx = i;
        }
    }
    var subset = [];
    subset.push(nums[idx]);
    while (prev[idx] !== -1){
        idx = prev[idx];
        subset.push(nums[idx]);
    }
    return subset;
};
