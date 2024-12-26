import java.util.Arrays;
import java.util.HashMap;
import java.util.Stack;

public class Solution {

    public int[] nextGreaterElement2(int[] nums1, int[] nums2) {

        HashMap<Integer, Integer> firstArrayHashMap = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums1.length; i++)
            firstArrayHashMap.put(nums1[i], i);

        int[] ans = new int[nums1.length];
        Stack<Integer> st = new Stack<>();
        for (int i = 0; i < nums2.length; i++)
        {
            int num2 = nums2[i];
            while (!st.isEmpty() && st.peek() < num2)
            {
                if (firstArrayHashMap.containsKey(st.peek()))
                    ans[firstArrayHashMap.get(st.pop())] = num2;
                else
                    st.pop();
            }
            if (firstArrayHashMap.containsKey(num2))
                st.push(num2);
        }

        while (!st.isEmpty())
            ans[firstArrayHashMap.get(st.pop())] = -1;

        return ans;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums1 = {4, 1, 2};
        int[] nums2 = {1, 3, 4, 2};
        int[] result = solution.nextGreaterElement2(nums1, nums2);
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}