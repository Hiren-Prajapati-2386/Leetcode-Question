class Solution {
    public int[][] flipAndInvertImage(int[][] image) {

        int n = image.length;
        
        for (int i = 0; i < n; i++) {
            int low = 0;
            int high = n - 1;
            
            while (low <= high) {
                if (image[i][low] == image[i][high]) {
                    int newVal = 1 - image[i][low];
                    image[i][low] = newVal;
                    image[i][high] = newVal;
                }
                low++;
                high--;
            }
        }
        
        return image;
        
    }
}