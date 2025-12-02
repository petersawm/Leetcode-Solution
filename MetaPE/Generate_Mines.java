package MetaPE;

import java.util.*;

/**
 * 在xLen * yLen的棋盘上随机生成mineNum个地雷
 * 因为地雷生成是随机的，可能会多次选中同一个位置，为了防止重复，需要一种方法确保每个地雷的位置都是唯一的
 * 用Fiser-Yates算法生成地雷
 * Time: O(n), Space: O(n)
 */

class Generate_Mines {
  public static int[][] generateMines(int xLen, int yLen, int mineNum) {
    int[][] res = new int[yLen][xLen];
    int[] pos = new int[xLen * yLen];
    for (int i = 0; i < pos.length; i++) {
      pos[i] = i;
    }

    // 随机生成前mineNum个地雷的位置
    Random random = new Random();
    for (int i = 0; i < mineNum; i++) {
      // 随机选取一个索引范围[i, pos.length - 1]内的元素
      int randomIndex = i + random.nextInt(pos.length - i);
      // 交换当前位置和随机位置的值
      int chosenPos = pos[randomIndex];
      pos[randomIndex] = pos[i];
      pos[i] = chosenPos;
      // 将选中的地雷位置映射回2D棋盘
      int row = chosenPos / xLen;
      int col = chosenPos % xLen;
      res[row][col] = -1; // MINE_MARK
    }
    return res;
  }
}

// public class Generate_Mines {
//   private static final int MINE_MARK = -1;

//   public static int[][] generateMines(int xLen, int yLen, int mineNum) {
//     // 用来存储已经选中的位置和替代位置
//     Map<Integer, Integer> map = new HashMap<>();
//     int[][] res = new int[xLen][yLen];
//     // means the valid position, range from 0 to range - 1
//     int range = yLen * xLen;

//     while (mineNum-- > 0) {
//       // Math.random()生成[0, 1)之间的随机数,再将这个放大到[0, range), 表示棋盘中位置的索引
//       // range--, 每次选中一个位置后随机范围不断缩小, 避免重复选择已经分配的地雷位置
//       int chosen = (int) (Math.random() * range--);
//       // 用map检查随机选择的chosen是否已经被分配, 如果被分配, 则返回map.get(chosen)的替代位置
//       // 如果没有被分配,则map.getOrDefault(chosen, chosen)返回chosen
//       int finalChosen = map.getOrDefault(chosen, chosen);
//       // 将当前的随机位置chosen映射到最后一个可用位置range
//       // 将所有可用映射到一组连续的索引中, 减少冲突
//       map.put(chosen, map.getOrDefault(range, range));
//       // 相当于是res[row][col] = MINE_MARK
//       res[finalChosen / xLen][finalChosen % xLen] = MINE_MARK;
//     }
//     return res;
//   }
// }