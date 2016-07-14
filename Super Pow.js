/**
 * @param {number} a
 * @param {number[]} b
 * @return {number}
 */


var superPow = function(a, b) {
    var c = 1337;
    var getMod = function(v, k){
        var t = 1;
        while (k --){
            t = (t * v) % c;
        }
        return t;
    }
    var base = getMod(a, 10);
    var d = 1;

    var l = b.length;
    var ret = 1;
    for (var i = l - 1 ; i >= 0 ; i --){

        if (i === l - 1){
            d = a;
        }
        else{
            d = getMod(d, 10);
            d %= c;
        }
        ret *= getMod(d, b[i]);
        ret %= c;
    }
    return ret;
};

console.log( superPow(2, [1,1]) );
