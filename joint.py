import ffmpeg

# 映像の読み込み
instream_v = ffmpeg.input("sample.mp4")

# 音声の読み込み
instream_a = ffmpeg.input("sample.mp3")

# コーデックと出力ファイルの指定
stream = ffmpeg.output(instream_v, instream_a,
                       "video_and_audio.mp4", vcodec="copy", acodec="copy")
# 実行
ffmpeg.run(stream)
