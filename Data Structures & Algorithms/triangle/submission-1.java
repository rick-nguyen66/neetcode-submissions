class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        for (int i = triangle.size() - 2; i >= 0; i--) {
            for (int j = 0; j < triangle.get(i).size(); j++) {
                int l = triangle.get(i + 1).get(j);
                int r = triangle.get(i + 1).get(j + 1);
                int minVal = triangle.get(i).get(j) + Math.min(l, r);
                triangle.get(i).set(j, minVal);
            }
        }
        return triangle.get(0).get(0);
        
        // return triangle.get(0).get(0) + 
        //         Math.min(minRec(triangle, 1, 0), minRec(triangle, 1, 1));
    }

    // public int minRec(List<List<Integer>> triangle, int r, int c) {
    //     if (r >= triangle.size() || c >= triangle.get(r).size()) {
    //         return 0;
    //     }
    //     return Math.min(triangle.get(r).get(c) + minRec(triangle,  r + 1, c), 
    //                     triangle.get(r).get(c) + minRec(triangle, r + 1, c + 1));
    // }
}