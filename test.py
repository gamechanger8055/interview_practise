# from enum import Enum
#
#
# # models
# class DifficultyLevel(Enum):
#     LOW, MEDIUM, HIGH = 1, 2, 3
#
#
# class Users:
#     def __init__(self, username):
#         self.username = username
#         self.score = 0
#         self.solved_questions = []
#
#
# class Questions:
#     def __init__(self, ids, score, level):
#         self.id = ids
#         self.level = level
#         self.score = score
#
#
# class Contest:
#     def __init__(self, creator, name, level):
#         self.creator = creator
#         self.name = name
#         self.level = level
#         self.participants = []
#         self.questions = []
#
#
# class CodingPlatform:
#     def __init__(self):
#         self.users = {}
#         self.contest = {}
#         self.questions = {}
#
#     # insert into users values();
#     def create_user(username):
#         self.users[username] = Users(username)
#
#     # insert into questions values();
#     def create_question(level, score):
#         if level not in self.questions:
#             self.questions[level] = Questions(score, level)
#         else:
#             self.questions[level].append(Questions(score, level))
#
#     # select * from questions where level='';
#     def list_questions(level):
#         return self.questions[level]
#
#     # insert into contest values();
#     def create_contest(name, level, creator):
#         if level not in self.contest:
#             self.contest[level] = Contest(creator, name, level)
#         else:
#             self.contest[level].append(Contest(creator, name, level))
#
#     # select * from contest where level='';
#
#     def list_contest(level):
#         return self.contest[level]
#
#     # update users set u.score=u.score+score from users where score in (select score from questions);
#     def solve_question(username, question):
#         if question not in self.users[username].solved_questions:
#             self.users[username].solved_questions.append(question)
#             self.users[username].score += question.score
#         else:
#             print("Question already solved")
#
#     # specific to users
#     # select from users order by score desc;
#     def leaderboard():
#         users = sorted(self.users, key=user.score)
#
#     def attend_contest(username, constest_name):
#         for level in self.contest:
#             for contest in self.contest[level]:
#                 if contest.name == constest_name and username not in contest.participants:
#                     contest.participants.append(username)
#
#     def run_contest(contest_name):
#         for level in self.contest:
#             for contest in self.contest[level]:
#                 if contest.name == constest_name:
#                     participant = sorted(contest.participants, key=contest.participants.score, reverse=True)
#
#
# Shubhankar
# Mrinal
# R2
#
# Coding
# Platform
# that
# allows
# a
# user
# to
# Sign
# Up, Create
# Contests and participate in Contests
# hosted
# by
# Others.
#
# Each
# contest
# can
# have
# a
# level(LOW, MEDIUM, HIGH) and will
# contain
# a
# set
# of
# questions.
#
# Each
# question
# will
# have
# different
# levels
# of
# difficulty(LOW, MEDIUM, HIGH) and score.
#
# Based
# on
# the
# contest
# level, the
# question
# set is going
# to
# be
# decided.Contest
# level
# with LOW difficulty will have questions with LOW difficulty level.
#
# Final
# score
# will
# be
# decided
# based
# on
# the
# difficulty
# LEVEL
# chosen
# for a contest
#
# Users
# solve
# problems and get
# points
# based
# on
# the
# difficulty
# of
# the
# problems and after
# the
# contests
# scores
# of
# the
# users
# are
# updated.
#
# Models
#
# Enums
# DifficultyLevel
# -LOW
# -MEDIUM
# -HARD
#
# Questions
# -id
# -difficulty
# level
# -score
#
# // crud
# op
#
# Users
# -id
# -username
# -ind_score
#
# // crud
# op
#
# Contest
# -id
# -questions[]
# Users[]
# level
#
# Methods
# signup()
# create_contest()
# participate()
# leaderboard()
# solve_question(username, question)
#
# Expected
# Methods
# CreateUser < user_name >
# CreateQuestion < difficulty_level, score >
# ListQuestion < difficulty_level >
# CreateContest < contest_name > < contest_level > < contest_creator_user_name >
# ListContest < difficulty_level >
# AttendContest < contest_id > < user_name >
# RunContest < contest_id > < contest_creator_user_name > // last
# LeaderBoard < sorting
# order
# asc / desc >
# ContestHistory < contest_id >
# WithdrawContest < contest_id >
#
# from enum import Enum
#
#
# # models
# class DifficultyLevel(Enum):
#     LOW, MEDIUM, HIGH = 1, 2, 3
#
#
# class Users:
#     def __init__(self, username):
#         self.username = username
#         self.score = 0
#         self.solved_questions = []
#
#
# class Questions:
#     def __init__(self, ids, score, level):
#         self.id = ids
#         self.level = level
#         self.score = score
#
#
# class Contest:
#     def __init__(self, creator, name, level):
#         self.creator = creator
#         self.name = name
#         self.level = level
#         self.participants = []
#         self.questions = []
#
#
# class CodingPlatform:
#     def __init__(self):
#         self.users = {}
#         self.contest = {}
#         self.questions = {}
#
#     # insert into users values();
#     def create_user(username):
#         self.users[username] = Users(username)
#
#     # insert into questions values();
#     def create_question(level, score):
#         if level not in self.questions:
#             self.questions[level] = Questions(score, level)
#         else:
#             self.questions[level].append(Questions(score, level))
#
#     # select * from questions where level='';
#     def list_questions(level):
#         return self.questions[level]
#
#     # insert into contest values();
#     def create_contest(name, level, creator):
#         if level not in self.contest:
#             self.contest[level] = Contest(creator, name, level)
#         else:
#             self.contest[level].append(Contest(creator, name, level))
#
#     # select * from contest where level='';
#
#     def list_contest(level):
#         return self.contest[level]
#
#     # update users set u.score=u.score+score from users where score in (select score from questions);
#     def solve_question(username, question):
#         if question not in self.users[username].solved_questions:
#             self.users[username].solved_questions.append(question)
#             self.users[username].score += question.score
#         else:
#             print("Question already solved")
#
#     # specific to users
#     # select from users order by score desc;
#     def leaderboard():
#         users = sorted(self.users, key=user.score)
#
#     def attend_contest(username, constest_name):
#         for level in self.contest:
#             for contest in self.contest[level]:
#                 if contest.name == constest_name and username not in contest.participants:
#                     contest.participants.append(username)
#
#     # def run_contest(contest_name):
#     #     for level in self.contest:
#     #         for contest in self.contest[level]:
#     #             if contest.name == constest_name:
#     #                 participant = sorted(contest.participants, key=contest.participants.score, reverse=True)
#
#
#
#
#
#
#
#
#
