from flask import Flask, render_template, request

app = Flask(__name__)

hdrs_questions = [
      {
        'sl': 1,
        'title': "Falling Asleep",
        'options': [
            {'label': "I never take longer than 30 minutes to fall asleep.", 'value': 0},
            {'label': "I take at least 30 minutes to fall asleep, less than half the time.", 'value': 1},
            {'label': "I take at least 30 minutes to fall asleep, more than half the time.", 'value': 2},
            {'label': "I take more than 60 minutes to fall asleep, more than half the time.", 'value': 3},
        ],
    },
    {
        'sl': 2,
        'title': "Sleep During the Night",
        'options': [
            {'label': "I do not wake up at night.", 'value': 0},
            {'label': "I have a restless, light sleep with a few brief awakenings each night.", 'value': 1},
            {'label': "I wake up at least once a night, but I go back to sleep easily.", 'value': 2},
            {'label': "I awaken more than once a night and stay awake for 20 minutes or more, more than half the time.", 'value': 3},
        ],
    },
    {
        'sl': 3,
        'title': "Waking Up Too Early",
        'options': [
            {'label': "Most of the time, I awaken no more than 30 minutes before I need to get up.", 'value': 0},
            {'label': "More than half the time, I awaken more than 30 minutes before I need to get up.", 'value': 1},
            {'label': "I almost always awaken at least one hour or so before I need to, but I go back to sleep eventually.", 'value': 2},
            {'label': "I awaken at least one hour before I need to, and can't go back to sleep.", 'value': 3},
        ],
    },
    {
        'sl': 4,
        'title': "Sleeping Too Much",
        'options': [
            {'label': "I sleep no longer than 7-8 hours/night, without napping during the day.", 'value': 0},
            {'label': "I sleep no longer than 10 hours in a 24-hour period including naps.", 'value': 1},
            {'label': "I sleep no longer than 12 hours in a 24-hour period including naps.", 'value': 2},
            {'label': "I sleep longer than 12 hours in a 24-hour period including naps.", 'value': 3},
        ],
    },
    {
        'sl': 5,
        'title': "Feeling Sad",
        'options': [
            {'label': "I do not feel sad.", 'value': 0},
            {'label': "I feel sad less than half the time.", 'value': 1},
            {'label': "I feel sad more than half the time.", 'value': 2},
            {'label': "I feel sad nearly all of the time.", 'value': 3},
        ],
    },
    {
        'sl': 6,
        'title': "Decreased Appetite",
        'options': [
            {'label': "There is no change in my usual appetite.", 'value': 0},
            {'label': "I eat somewhat less often or lesser amounts of food than usual.", 'value': 1},
            {'label': "I eat much less than usual and only with personal effort.", 'value': 2},
            {'label': "I rarely eat within a 24-hour period, and only with extreme personal effort or when others persuade me to eat.", 'value': 3},
        ],
    },
    {
        'sl': 7,
        'title': "Increased Appetite",
        'options': [
            {'label': "There is no change from my usual appetite.", 'value': 0},
            {'label': "I feel a need to eat more frequently than usual.", 'value': 1},
            {'label': "I regularly eat more often and/or greater amounts of food than usual.", 'value': 2},
            {'label': "I feel driven to overeat both at mealtime and between meals.", 'value': 3},
        ],
    },
    {
        'sl': 8,
        'title': "Decreased Weight (Within the Last Two Weeks)",
        'options': [
            {'label': "I have not had a change in my weight.", 'value': 0},
            {'label': "I feel as if I've had a slight weight loss.", 'value': 1},
            {'label': "I have lost 2 pounds or more.", 'value': 2},
            {'label': "I have lost 5 pounds or more.", 'value': 3},
        ],
    },
    {
        'sl': 9,
        'title': "Increased Weight (Within the Last Two Weeks)",
        'options': [
            {'label': "I have not had a change in my weight.", 'value': 0},
            {'label': "I feel as if I've had a slight weight gain.", 'value': 1},
            {'label': "I have gained 2 pounds or more.", 'value': 2},
            {'label': "I have gained 5 pounds or more.", 'value': 3},
        ],
    },
    {
        'sl': 10,
        'title': "Concentration/Decision Making",
        'options': [
            {'label': "There is no change in my usual capacity to concentrate or make decisions.", 'value': 0},
            {'label': "I occasionally feel indecisive or find that my attention wanders.", 'value': 1},
            {'label': "Most of the time, I struggle to focus my attention or to make decisions.", 'value': 2},
            {'label': "I cannot concentrate well enough to read or cannot make even minor decisions.", 'value': 3},
        ],
    },
    {
        'sl': 11,
        'title': "View of Myself",
        'options': [
            {'label': "I see myself as equally worthwhile and deserving as other people.", 'value': 0},
            {'label': "I am more self-blaming than usual.", 'value': 1},
            {'label': "I largely believe that I cause problems for others.", 'value': 2},
            {'label': "I think almost constantly about major and minor defects in myself.", 'value': 3},
        ],
    },
    {
    'sl': 13,
    'title': 'General Interest',
    'options': [
        {
            'label': "There is no change from usual in how interested I am in other people or activities",
            'value': 0,
        },
        {
            'label': "I notice that I am less interested in people or activities.",
            'value': 1,
        },
        {
            'label': "I find I have interest in only one or two of my formerly pursued activities.",
            'value': 2,
        },
        {
            'label': "I have virtually no interest in formerly pursued activities.",
            'value': 3,
        },
    ],
},
{
    'sl': 14,
    'title': 'Energy Level',
    'options': [
        {
            'label': "There is no change in my usual level of energy",
            'value': 0,
        },
        {
            'label': "I get tired more easily than usual.",
            'value': 1,
        },
        {
            'label': "I have to make a big effort to start or finish my usual daily activities (for example, shopping, homework, cooking or going to work).",
            'value': 2,
        },
        {
            'label': "I really cannot carry out most of my usual daily activities because I just don't have the energy..",
            'value': 3,
        },
    ],
},
{
    'sl': 15,
    'title': 'Feeling slowed down',
    'options': [
        {
            'label': "I think, speak, and move at my usual rate of speed.",
            'value': 0,
        },
        {
            'label': "I find that my thinking is slowed down or my voice sounds dull or flat.",
            'value': 1,
        },
        {
            'label': "It takes me several seconds to respond to most questions and I'm sure my thinking is slowed.",
            'value': 2,
        },
        {
            'label': "I am often unable to respond to questions without extreme effort.",
            'value': 3,
        },
    ],
},
{
    'sl': 16,
    'title': 'Feeling restless',
    'options': [
        {
            'label': "I do not feel restless.",
            'value': 0,
        },
        {
            'label': "I'm often fidgety, wringing my hands, or need to shift how I am sitting.",
            'value': 1,
        },
        {
            'label': "I have impulses to move about and am quite restless.",
            'value': 2,
        },
        {
            'label': "At times, I am unable to stay seated and need to pace around.",
            'value': 3,
        },
    ],
}

  
]

@app.route('/quiz', methods=['POST'])
def quiz():
    results = []
    for i in range(len(hdrs_questions)):
        question = hdrs_questions[i]
        selected_answer = request.form.get(str(i))
        results.append({'question': question['title'], 'selectedAnswer': selected_answer})

    total_score = sum(int(result['selectedAnswer']) for result in results)

    range_label, message = get_score_range(total_score)

    return render_template('results.html', total_score=total_score, range_label=range_label, message=message)

def get_score_range(total_score):
    if 0 <= total_score <= 5:
        return '0-5', 'You are doing great!'
    elif 6 <= total_score <= 10:
        return '6-10', 'You\'re doing well, keep it up!'
    elif 11 <= total_score <= 15:
        return '11-15', 'You may want to pay attention to some aspects of your well-being.'
    else:
        return '16-20', 'It\'s advisable to seek professional help. Take care of yourself.'

if __name__ == '__main__':
    app.run(debug=True)
