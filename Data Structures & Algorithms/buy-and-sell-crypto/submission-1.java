class Solution {
    public int maxProfit(int[] prices) {
        int cheapest_so_far = prices[0];
        int max_profit =0;
        for (int i = 0; i <= prices.length - 1; i++){
            if (prices[i] < cheapest_so_far) {
                cheapest_so_far = prices[i];
            } 
            else{
                if ((prices[i] - cheapest_so_far) >= max_profit){
                    max_profit = prices[i] - cheapest_so_far;
                } 
            }
        }
        return max_profit;
    }
}
