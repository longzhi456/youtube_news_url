import os
import yt_dlp

def fetch_m3u8_url(youtube_url):
  ydl_opts = {
        'format': 'best',  # 自动选择最佳质量格式
        'quiet': True,     # 关闭控制台输出(不显示下载进度等信息)
        'no_warnings': True,  # 隐藏警告信息
    }
  
  try:  # 异常处理模块开始
        # 创建YoutubeDL下载器实例（使用with确保资源释放）
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 提取视频/直播信息但不下载文件（download=False）
            info = ydl.extract_info(youtube_url, download=False)
            
            # 搜索可用格式列表 ---------------
            if 'formats' in info:  # 检查是否存在格式信息
                # 遍历所有可用格式
                for stream in info['formats']:
                    # 查找使用HLS协议的流（m3u8_native是HLS流的标识）
                    if stream.get('protocol') == 'm3u8_native':
                        return stream['url']  # 返回找到的M3U8地址
            
            # 如果未找到HLS流则尝试直接获取URL（备用方案）
            return info.get('url', '未找到M3U8地址')
    
    except Exception as e:  # 异常捕获
        return f'错误: {str(e)}'  # 返回可读的错误信息

if __name__ == "__main__":
    # 获取用户输入的YouTube链接
    url = input("请输入YouTube直播/视频URL: ")
    # 调用函数获取M3U8地址
    m3u8_url = fetch_m3u8_url(url)
    # 输出结果
    print("M3U8地址:", m3u8_url)
