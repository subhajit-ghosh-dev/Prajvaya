const fs = require('fs');
const path = require('path');

const logPath = 'C:/Users/DELL/.gemini/antigravity/brain/86b000d6-a8c5-4685-8a13-2ca2618c5bab/.system_generated/logs/transcript.jsonl';

try {
  const fileContent = fs.readFileSync(logPath, 'utf8');
  const lines = fileContent.split('\n');
  const targetLine = lines.find(line => {
    if(!line) return false;
    try {
      const obj = JSON.parse(line);
      return obj.step_index === 26;
    } catch(e) { return false; }
  });
  
  if (!targetLine) {
    console.error("No line found for step_index 26");
    process.exit(1);
  }
  
  const obj = JSON.parse(targetLine);
  const toolCall = obj.tool_calls[0];
  const codeContentEscaped = toolCall.args.CodeContent;
  
  let extractedCode = JSON.parse(codeContentEscaped);
  
  fs.writeFileSync('app.js.original', extractedCode, 'utf8');
  console.log("Successfully extracted app.js.original. Length:", extractedCode.length);
} catch (e) {
  console.error("Error occurred:", e);
}
