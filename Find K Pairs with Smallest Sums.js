 /**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number[][]}
 */


const INT_MAX = 1<<30;

var kSmallestPairs = function(nums1, nums2, k) {
    var results = [];
    if (!nums1.length || !nums2.length){
        return [];
    }
    var l1 = nums1.length, l2 = nums2.length;
    var unit = {u: 0, v: 0};
    var array = [];
    var hash = {};

    var pop = function(){
        if (array.length > 0){
            var ret = array[0];
            swap(0, array.length - 1);
            array.pop();
            minHeapify(0, array.length);
            return ret;
        }
    };

    var minHeapify = function(idx, size){
        var iMin = idx, iLeft = idx * 2 + 1, iRight = idx * 2 + 2;
        if (iLeft < size && array[iLeft].value < array[iMin].value){
            iMin = iLeft;
        }
        if (iRight < size && array[iRight].value < array[iMin].value){
            iMin = iRight;
        }
        if (iMin !== idx){
            swap(iMin, idx);
            minHeapify(iMin, size);
        }
    };

    var bubbleUp = function(idx){
        if (idx === 0){
            return;
        }
        var parentIdx = Math.floor((idx - 1)/2);
        if (array[parentIdx].value > array[idx].value){
            swap(idx, parentIdx);
            bubbleUp(parentIdx);
        }
    };

    var add = function(obj){
        if (hash[obj.u+':'+obj.v]){
            return;
        }
        hash[obj.u+':'+obj.v] = 1;
        array.push(obj);
        bubbleUp(array.length - 1);
    };

    var swap = function(i, j){
        var tmp = array[i];
        array[i] = array[j];
        array[j] = tmp;

    };

    var o = {u: 0, v: 0, value: nums1[0] + nums2[0]};
    add(o);

    while (k --){
        var temp = pop();
        if (!temp){
            break;
        }
        results.push( [nums1[temp.u] , nums2[temp.v]] );
        if (temp.v + 1 < l2){
            add({u: temp.u, v: temp.v+1, value: nums1[temp.u] + nums2[temp.v+1]});
        }
        if (temp.u + 1 < l1){
            add({u: temp.u + 1, v: temp.v, value: nums1[temp.u + 1] + nums2[temp.v]});
        }
    }

    return results;
};
