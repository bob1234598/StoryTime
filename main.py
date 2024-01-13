from flask import Flask, render_template, jsonify
import openai
import os

app = Flask(__name__)

# Ensure API key is set
if 'OPENAI_API_KEY' not in os.environ:
  print("OpenAI API key is not set.", file=sys.stderr)
  exit(1)

openai.api_key = os.environ['OPENAI_API_KEY']


@app.route('/')
def hello_world():
  try:
    response = openai.ChatCompletion.create(model="gpt-4",
                                            messages=[{
                                                "role":
                                                "system",
                                                "content":
                                                "Generate a story for small children without complex vocabulary and with happy end. Teach a moral lesson with the story. Start right with your story, without 'here is a story'"
                                            }])
    story = response.choices[0].message.content
  except Exception as e:
    story = "Error fetching story: " + str(e)

  return render_template('index.html', story=story)

@app.route('/get_new_story')
def get_new_story():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{
                "role": "system",
                "content": "Generate a story for small children without complex vocabulary and with happy end. Teach a moral lesson with the story. Start right with your story, without 'here is a story'"
            }]
        )
        story = response.choices[0].message.content
    except Exception as e:
        story = "Error fetching story: " + str(e)

    return jsonify({'story': story})


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000, debug=True)
