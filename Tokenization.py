import nltk
nltk.download
nltk.download("punkt")


paragraph = "In writing, the words point and purpose are almost synonymous. Your point is your purpose, and how you decide to make your point clear to your reader is also your purpose. Writers have a point and a purpose for every paragraph that they create.Writers write descriptive paragraphs because their purpose is to describe something. Their point is that something is beautiful or disgusting or strangely intriguing. Writers write persuasive and argument paragraphs because their purpose is to persuade or convince someone. Their point is that their reader should see things a particular way and possibly take action on that new way of seeing things. Writers write paragraphs of comparison because the comparison will make their point clear to their readers.The purpose of Pattern Based Writing: Quick & Easy Essay is to quickly and easily teach students how to organize information and make points clear. Then in the Writing with Purpose section of the writing program, students learn to apply their new writing strategies to different types, kinds, genres, and modes of writing. The truth is that it’s quick and easy to get students to write many different types of paragraphs when they have the right foundation.Put simply, all of the different types and kinds of paragraphs simply involve layering on a different purpose or intent. When students have the right foundation, it’s just that simple. What are you trying to achieve in this paragraph and in your whole composition? What is your purpose right here? Do you wish to describe? Do you want to evaluate? Is your goal to narrate? Is your intent to persuade?"



sentences = nltk.sent_tokenize(paragraph)

#print(sentences)

words = nltk.word_tokenize(paragraph)

print(words)