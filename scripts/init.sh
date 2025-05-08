rm -rf ./store/voices*
huggingface-cli download onnx-community/Kokoro-82M-v1.0-ONNX --include "voices/jf_*.bin" --local-dir ./store/voices_tmp
mv ./store/voices_tmp/voices ./store/voices
rm -rf ./store/voices_tmp
huggingface-cli download onnx-community/Kokoro-82M-v1.0-ONNX --include "onnx/model.onnx" --local-dir ./store/onnx_tmp
mv ./store/onnx_tmp/onnx/model.onnx ./store/model.onnx
rm -rf ./store/onnx_tmp
python -m unidic download