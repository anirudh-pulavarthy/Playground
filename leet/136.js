/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let ans = 0;

    for (let x of nums)
        ans = ans ^ x;
    
    return ans;
};