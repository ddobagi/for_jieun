const express = require('express');
const { exec } = require('child_process');
const app = express();
const PORT = process.env.PORT;

app.use(express.json());

app.get('/run-selenium', (req, res) => {
    res.send("working ✅ 서버 잘 살아있습니다!");
  });  

app.post('/run-selenium', (req, res) => {
  exec('python script.py', (error, stdout, stderr) => {
    if (error) {
      console.error(`[오류] ${error.message}`);
      return res.status(500).send("셀레니움 실행 실패");
    }
    if (stderr) {
      console.error(`[stderr] ${stderr}`);
    }

    console.log(`[stdout] ${stdout}`);
    res.send("셀레니움 실행 완료!");
  });
});

app.listen(PORT, () => {
  console.log(`Express 서버 실행 중`);
});
