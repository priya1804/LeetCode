<?php
// Define a Solution class
class Solution {
    // Method to calculate the minimum number of bit flips
    public function minBitFlips($start, $goal) {
        // XOR the two numbers and count the number of 1s in the result
        $xorResult = $start ^ $goal;
        
        // Count the number of 1s in the binary representation of the XOR result
        $count = 0;
        while ($xorResult > 0) {
            $count += $xorResult & 1; // Increment count if the least significant bit is 1
            $xorResult >>= 1;          // Right shift the bits of xorResult
        }
        
        return $count;
    }
}

// Test the function with the provided examples
$testCases = [
    [10, 7],  // Expected output: 3
    [3, 4],   // Expected output: 3
];

// Instantiate the Solution class
$solution = new Solution();

// Run the test cases
foreach ($testCases as $test) {
    list($start, $goal) = $test;
    echo "start: $start, goal: $goal -> flips: " . $solution->minBitFlips($start, $goal) . "\n";
}
?>
