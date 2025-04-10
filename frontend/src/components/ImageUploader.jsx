import { useEffect, useRef } from 'react';
import { FaceMesh } from '@mediapipe/face_mesh';
import { Camera } from '@mediapipe/camera_utils';

export default function ImageUploader({ onAnalysis }) {
  const videoRef = useRef();
  const canvasRef = useRef();

  useEffect(() => {
    const faceMesh = new FaceMesh({
      locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/${file}`
    });

    faceMesh.setOptions({
      maxNumFaces: 1,
      minDetectionConfidence: 0.5
    });

    faceMesh.onResults((results) => {
      if (results.multiFaceLandmarks) {
        const canvas = canvasRef.current;
        canvas.getContext('2d').drawImage(videoRef.current, 0, 0);
        const image = canvas.toDataURL('image/jpeg');
        onAnalysis(image);
      }
    });

    const camera = new Camera(videoRef.current, {
      onFrame: async () => {
        await faceMesh.send({ image: videoRef.current });
      },
      width: 640,
      height: 480
    });
    camera.start();

    return () => camera.stop();
  }, []);

  return (
    <div className="relative">
      <video ref={videoRef} className="rounded-lg" autoPlay playsInline />
      <canvas ref={canvasRef} width="640" height="480" className="hidden" />
    </div>
  );
}