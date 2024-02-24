package hash;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class 프로그래머스_폰켓몬 {

    public int solution(int[] nums) {
        int max = nums.length / 2;

        long count = Arrays.stream(nums).boxed().distinct().count();


        // 중복을 제거한 셋의 크기가 max보다 크면 max를, 작으면 numsSet의 size를 리턴
        if (count > max) {
            return max;
        } else {
            return (int)count;
        }
    }

    @Test
    public void 정답() {
        Assertions.assertEquals(2, solution(new int[]{3, 1, 2, 3}));
    }
}
