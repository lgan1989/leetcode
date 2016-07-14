 /**
 * @param {number} num
 * @return {boolean}
 */

var isPerfectSquare = function(num){
    var low = 1;
    var high = num;
    if (num === 1){
        return true;
    }
    for (var i = 0 ; i < 32 ; i ++){
        var mid = low + ((high - low)>>1);
        if (num % mid === 0 && num/mid === mid){
            return true;
        }
        var ret = num / mid;
        if (ret > mid){
            low = mid + 1;
        }
        else{
            high = mid - 1;
        }
    }
    return false;
}
