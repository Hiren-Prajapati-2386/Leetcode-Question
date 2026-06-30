class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

        int i = 0;
        int j = 0;
        int k = 0;
        int n = nums1.length;
        int m = nums2.length;

        int[] merge = new int[n+m];

        while (i < n && j < m){
            if(nums1[i] >= nums2[j]){
                merge[k++] = nums2[j++];
            }
            else{
                merge[k++] = nums1[i++];
            }
        }

        while (i < n){
            merge[k++] = nums1[i++];
        }
        while (j < m){
            merge[k++] = nums2[j++];
        }


        int m_len = merge.length;
        if(m_len % 2 == 0){

//            for even we have two median point
            int first = m_len/2;
            int second = m_len/2 - 1;

            double median_sum = merge[first] + merge[second];

            return median_sum/2.0;
        }
        else {

            int index = m_len/2;

            return merge[index];
        }

       
    }
        
}
