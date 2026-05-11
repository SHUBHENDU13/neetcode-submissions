class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    scoreOfString(s) {
        let ans = 0;
        const strArr = s.split('');
        for(let i = 0; i < strArr.length-1; i++){
            ans += Math.abs(strArr[i].charCodeAt(0) - strArr[i+1].charCodeAt(0));
        }
        return ans;
    }
}
