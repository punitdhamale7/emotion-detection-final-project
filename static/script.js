document.getElementById("emotion-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  const text = document.getElementById("textToAnalyze").value;
  const result = document.getElementById("result");

  const response = await fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(text)}`);
  const body = await response.text();

  if (!response.ok) {
    result.textContent = body;
    return;
  }

  const data = JSON.parse(body);
  result.textContent =
    `anger: ${data.anger}\n` +
    `disgust: ${data.disgust}\n` +
    `fear: ${data.fear}\n` +
    `joy: ${data.joy}\n` +
    `sadness: ${data.sadness}\n` +
    `dominant emotion: ${data.dominant_emotion}`;
});
