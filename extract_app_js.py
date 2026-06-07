import json

log_path = 'C:/Users/DELL/.gemini/antigravity/brain/86b000d6-a8c5-4685-8a13-2ca2618c5bab/.system_generated/logs/transcript.jsonl'

try:
    with open(log_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for line_idx, line in enumerate(lines):
        if not line:
            continue
        try:
            obj = json.loads(line, strict=False)
            step_idx = obj.get('step_index')
            
            tool_calls = obj.get('tool_calls', [])
            for tc in tool_calls:
                target_file = tc.get('args', {}).get('TargetFile', '')
                if 'app.js' in target_file:
                    print(f"Found app.js in line {line_idx}, step {step_idx}, tool {tc['name']}")
                    if tc['name'] == 'write_to_file':
                        code_content_escaped = tc['args']['CodeContent']
                        try:
                            # Try to parse
                            code = json.loads(code_content_escaped, strict=False)
                            filename = f'extracted_app_step_{step_idx}.js'
                            with open(filename, 'w', encoding='utf-8') as f_out:
                                f_out.write(code)
                            print(f"  Wrote {filename}. Length: {len(code)}")
                        except Exception as e_inner:
                            print(f"  Failed parsing inner for step {step_idx}: {str(e_inner)}")
        except Exception as e:
            print(f"  Failed parsing line {line_idx}: {str(e)}")
            
except Exception as e:
    import traceback
    traceback.print_exc()
