import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class main {
    public static void main(String[] args) {
        System.out.println("=== [Java] Neoforic 内核启动 ===");

        if (args.length > 0) {
            String jsonFileName = args[0];
            System.out.println("[Java] 准备读取清单文件: " + jsonFileName);
            readJsonFile(jsonFileName);
        } else {
            System.out.println("[Java] 警告：没有收到清单文件！");
        }
    }

    public static void readJsonFile(String fileName) {
        try {
            // 1. 直接把整个文件读成一个巨大的字符串
            String content = new String(Files.readAllBytes(Paths.get(fileName)), "UTF-8");

            // 2. 开启 DOTALL 模式，允许正则跨越换行符匹配
            Pattern pattern = Pattern.compile("\"type\"\\s*:\\s*\"([^\"]+)\"\\s*,\\s*\"id\"\\s*:\\s*\"([^\"]+)\"\\s*,\\s*\"jar_path\"\\s*:\\s*\"([^\"]+)\"", Pattern.DOTALL);

            Matcher matcher = pattern.matcher(content);
            int modCount = 0;

            // 3. 循环把所有的模组全找出来
            while (matcher.find()) {
                String type = matcher.group(1);
                String id = matcher.group(2);
                String jarPath = matcher.group(3);

                modCount++;
                System.out.println("  -> 发现模组 [" + id + "] 类型: " + type);
                System.out.println("     路径: " + jarPath);
            }
            System.out.println("\n[成功] Java 读取完毕，共解析了 " + modCount + " 个模组数据！");

        } catch (Exception e) {
            System.out.println("[错误] 无法读取文件: " + e.getMessage());
        }
    }
}