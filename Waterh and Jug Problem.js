/**
 * @param {number} x
 * @param {number} y
 * @param {number} z
 * @return {boolean}
 */

var gcd = function(a, b){
    while (a !== b){
        if (a < b){
            a ^= b , b ^= a, a ^= b;
        }
        a = a - b;
    }
    return a;
}

var canMeasureWater = function(x, y, z) {
    if (!z || x === z || y === z || x + y === z){
        return true;
    }
    if (x && y && !z)return false;
    if (!x && y !== z)return false;
    if (!y && x !== z)return false;
    return x + y > z && z % gcd(x,y) === 0;
};
