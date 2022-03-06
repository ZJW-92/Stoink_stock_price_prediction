## **Project management**


Purpose:<br>
To log meeting attendance and decisions.

We start meeting with standup, we discuss the progress achieved by each member, the existing issues, and ways to resolve them

---


### **Week 44**
No meetings<br>
Forming groups

---
### **Week 45**
#### **Meeting 8/11**.

**Missing:**<br>
none

**Decisions:**<br>
Meeting Mon 09:00-10:00 and Wed 12:00-13:00.<br>
Adding extra meetings if required.<br>
Started a Discord for communication and Trello board for Project Management.<br>
Deciding on 3 potential ideas.<br>

#### **Meeting 10/11**.

**Missing:**<br>
none

**Decisions:**<br>
Decided on Stock picking prediction.<br>
Distributed Assignment 1 into individual tasks.a<br>
All should install necessary software packages and libraries.<br>

| Task        | Responsible |
| ----------- | ----------- |
| Write concept      | Zhijie Wei       |
| Write requirments   | Effat Mahmud Enti        |
| Save API data in SQL and CSV file   | Samuel Gunnarsson        |
| Describe data and discuss validity for project   | Eemil Jeskanen        |
| Create a toy prediction model   | Eric Hallberg        |


**Agenda for next meeting:**<br>
Standup.<br>
check progression on Assingment 1 tasks.<br>
Decide on facilitator.<br>
Setup Gitlab repo.<br>

---
### **Week 46**
#### **Meeting 15/11**.

**Missing:**<br>
none

**Decisions:**<br>
Decided on facilitator and markdown reponsible.<br>
Choose a name for the project.<br>
Try to finish Assigment 1 tasks for Wed meeting.<br>
Study what balance sheet and LTSM NN is.<br>


| Task        | Responsible |
| ----------- | ----------- |
| Create markdown document   | Eric Hallberg        |


**Agenda for next meeting:**<br>
Standup.<br>
Finish Assignment 1 together.<br>
Discuss Deployment software for our system.<br>

#### **Meeting 17/11**.

**Missing:**<br>
none

**Discussions:**<br>
Deployment software.<br>
What type the label should be.<br>
What type of features we should use.<br>
file structure in the SQL database.<br>
What framework to use.<br>
Using CD/CI during the project in gitlab.<br>


**Decisions:**<br>
Individually look through assignment 1 and then have meeting on friday 13:30 to finish up and submit.<br>
ASk ta on tuesday about docker/kubernetes.<br>
Booking a room for next on campus meeting in SVEA.<br>
prediction will be the price difference in three months after latest balance sheet release.<br>


| Task        | Responsible |
| ----------- | ----------- |
|      |          |


**Agenda for next meeting 22/11:**<br>
Standup.<br>
Dicuss which features to use.<br>


---
### **Week 47**

#### **Meeting 22/11**.

**Missing:**<br>
none

**Discussions:**<br>
Topics and questions for TA-session 23/11.<br>
What features to use.<br>
Using pipenv for the rest of the project?.<br>


**Decisions:**<br>
Deciding to start on the front-end, setting up basic project.<br>
Make an intital UI design.<br>
Completing the database with monthly data (label).<br>


| Task        | Responsible |
| ----------- | ----------- |
| Mock-up Ui design      | Zhijie Wei       |
| Setup CI/CD   | Effat Mahmud Enti        |
| Load & save monthly data from API   | Samuel Gunnarsson        |
| Setup Django   | Eemil Jeskanen        |
| Create code to label the data correctly   | Eric Hallberg        |


**Agenda for next meeting 24/11:**<br>
Standup.<br>
Looking at Assignment 2.<br>


#### **Meeting 24/11**.

**Missing:**<br>
none

**Discussions:**<br>
Definition of done, how to handle merge requests<br>
Assigment 2.<br>
How to handle data in the database.<br>


**Decisions:**<br>
Create new branch called development, all branch out from this and then deal with ther own marge requests.
Every monday meeting we review the development branch and merge it to the main branch.<br>


| Task        | Responsible |
| ----------- | ----------- |
| Basic homepage setup      | Zhijie Wei       |
| Frontend prediction page     | Zhijie Wei       |
| Frontend admin page  | Samuel Gunnarsson        |
| Frontend Header and Footer   | Eemil Jeskanen        |
| Correlation analysis on data  | Eric Hallberg        |


**Agenda for next meeting 29/11:**<br>
Standup.<br>
Feedback A1

---
### **Week 48**

#### **Meeting 29/11**.

**Missing:**<br>
Effat Mahmud Enti.<br>

**Discussions:**<br>
Correlation analysis result.<br>
Added additonal data, Income statement, earnings and cash flow.<br>
How to handle data in the database.<br>
What to ask during supervision session 30/11.<br>


**Decisions:**<br>
Add descriptio to homepage.<br>
Wait with merging dev into main after SV-session.<br>
Ask Ta about what features is good enough, SV-session.<br>


| Task        | Responsible |
| ----------- | ----------- |
| Correlation analysis on all features  | Eric Hallberg        |


**Agenda for next meeting 1/12:**<br>
Standup.<br>

#### **Meeting 1/12**.

**Missing:**<br>
None.<br>

**Discussions:**<br>
After a member dropout we need to be really requirment oriented when making tasks, try to get a product to show on the fair.<br>
Discussion about what fetures to use.<br>
Discussion about how we feel about our progress.<br>


**Decisions:**<br>
Starting an intial model based on the current best features.<br>
Secided to try % on our features, so the difference between reports, as new features.<br>
Merging dev branch into main on monday.<br>


| Task        | Responsible |
| ----------- | ----------- |
| Make initial model      | Zhijie Wei       |
| Make initial model      | Effat Mahmud Enti       |
| Frontend admin page  | Samuel Gunnarsson        |
| 10 best feature into a CSV file (for the model)  | Eric Hallberg        |
| Change all features to % increase and make correlation analysis  | Eric Hallberg        |

**Agenda for next meeting 6/12:**<br>
Standup.<br>


---
### **Week 49**

#### **Meeting 6/12**.

**Missing:**<br>
Effat Mahmud Enti.<br>

**Discussions:**<br>
What model fits our problem best.<br>
Discussion about what fetures to use.<br>
Structure of the entire project.<br>


**Decisions:**<br>
Adding features of market type for each stock/company.<br>
Try to install kubernetes.<br>
Decide next Ta meeting about features.<br>
merging Dev into main.<br>


| Task        | Responsible |
| ----------- | ----------- |
| Add market category as a feature to the dataset  | Eric Hallberg        |
| Change all data in features to % difference since last report  | Eric Hallberg        |


**Agenda for next meeting 8/12:**<br>
Standup.<br>
Decide which model to use.<br>

#### **Meeting 8/12**.

**Missing:**<br>
None.<br>

**Discussions:**<br>
What task are left to focus on.<br>
Discussion about testing.<br>



**Decisions:**<br>
Discarding the idea of LSTM.<br>
Ask Ta about, Testing and model types.<br>



| Task        | Responsible |
| ----------- | ----------- |
| Start and experiment with model      | All members      |
| Fix data cleaning file and put in project  | Eric Hallberg        |

**Agenda for next meeting 10/12:**<br>
Standup.<br>
Decide on a model and deploy it for now.<br>
Check Assignment description and add tasks accodring.<br>


#### **Extra Meeting 10/12**.

**Missing:**<br>
None.<br>

**Discussions:**<br>
What task are left to focus on.<br>
Discussion about testing.<br>


**Decisions:**<br>
made task cards i trello from the remaining requirments.<br>
Decide on a intial model to deploy.<br>



| Task        | Responsible |
| ----------- | ----------- |
| Start and experiment with model      | All members      |


**Agenda for next meeting 13/12:**<br>
Standup.<br>
Decide on a model and deploy it for now.<br>
Check Assignment description and add tasks accodring.<br>



---
### **Week 50**
#### **Meeting 13/12**.

**Missing:**<br>
Effat Mahmud Enti.<br>

**Discussions:**<br>
datastorage, store clean or raw data in db.<br>
discussing the meaning of dynamic training of model via admin page.<br>
How good does the model need to be.<br>



**Decisions:**<br>
Ask TA about the 3 things we discussed.<br>



| Task        | Responsible |
| ----------- | ----------- |
| Code functions in models.py for training, evaluating and predicting.   |   Eric Hallberg    |


**Agenda for next meeting 15/12:**<br>
Standup.<br>


#### **Meeting 15/12**.

**Missing:**<br>
Zhijie Wei.<br>

**Discussions:**<br>
Planning the structure for the fair presentation.<br>
What is left to do.<br>

**Decisions:**<br>
splitting the presentation between the members<br>



| Task        | Responsible |
| ----------- | ----------- |
| Idea, Data Source, Architecture   |  Samuel Gunnarsson      |
| Fronted, To Do, Obstacles   |  Effat Mahmud Enti      |
| Data Processing, Ml pipeline, Live Demo   |  Eric Hallberg     |
| Unit test datacleaning function   |  Eric Hallberg     |


**Agenda for next meeting 20/12:**<br>
Standup.<br>


---
### **Week 51**

#### **Meeting 20/12**.

**Missing:**<br>
Effat Mahmud Enti.<br>

**Discussions:**<br>
Planning the structure for the fair presentation.<br>
What is left to do.<br>

**Decisions:**<br>
Moving Wednesday 22/12 meeting to 09:00.<br>


| Task        | Responsible |
| ----------- | ----------- |
| loading and saving the model as Django model   |  Eric Hallberg     |
| Setup basic Admin page   |  Eric Hallberg     |
| Showing results and attributes of evaluation/retraining in the admin page in Admin.py |  Eric Hallberg     |

**Agenda for next meeting 22/12:**<br>
Standup.<br>

#### **Meeting 22/12**.

**Missing:**<br>
Effat Mahmud Enti.<br>

**Discussions:**<br>
Dividing more tasks<br>

**Decisions:**<br>
Keep meetings as usual during the holidays.<br>


| Task        | Responsible |
| ----------- | ----------- |
| Upload via admin page an CSv file with cleaned data  |  Eric Hallberg     |
| add func to deploy a model, with deployment button in admin page   |  Eric Hallberg     |
| add evaluate and retrain func with buttons in admin page   |  Eric Hallberg     |
| fix price into percentage value in stock and all stocks page   |  Zhiijie Wei     |
| Deploy system on kubernetes   |  Samuel Gunnarsson     |
| Load data into Django models & query the database |  Samuel Gunnarsson     |



**Agenda for next meeting 29/12:**<br>
Standup.<br>


---
### **Week 52**
#### **Meeting 27/12**.

**Missing:**<br>
Effat Mahmud Enti.<br>

**Discussions:**<br>
progress so far.<br>
Discussing Unit testing.<br>

**Decisions:**<br>
dividing tasks<br>


| Task        | Responsible |
| ----------- | ----------- |
| update markdown  |  Eric Hallberg     |
| redo allstocks page  |  Zhiijie Wei     |
| finish and implement k8s   |  Samuel Gunnarsson     |


**Agenda for next meeting 27/12:**<br>
Standup.<br>

#### **Meeting 29/12**.

**Missing:**<br>
Effat Mahmud Enti.<br>

**Discussions:**<br>
progress so far.<br>
Discussing Unit testing.<br>

**Decisions:**<br>
dividing tasks<br>


| Task        | Responsible |
| ----------- | ----------- |
| fix unit test Check columns cleaned data  |  Eric Hallberg     |
| Unit test, train_model()   |  Samuel Gunnarsson     |
| Unit test, allstocks, predict and testFunc   |  Zhiijie Wei     |

**Agenda for next meeting 3/1:**<br>
Standup.<br>

---
### **Week 1**

#### **Meeting 3/1**.

**Missing:**<br>
Effat Mahmud Enti.<br>

**Discussions:**<br>
progress so far.<br>
Discussing Unit testing.<br>
Model versioning and loading.<br>

**Decisions:**<br>
dividing tasks<br>
Start report latest Thursday.<br>

| Task        | Responsible |
| ----------- | ----------- |
| solve name issues with .h5  |  Eric Hallberg     |
| Diagrams for report  |  Samuel Gunnarsson     |
| Unit test, evaluate_model()    |  Samuel Gunnarsson     |

**Agenda for next meeting 5/1:**<br>
Standup.<br>
plan for A2 writing.<br>

#### **Meeting 5/1**.

**Missing:**<br>
Effat Mahmud Enti.<br>

**Discussions:**<br>
Repo and files and folders structure<br>
Discussing Unit testing.<br>
REport structuring<br>

**Decisions:**<br>
dividing tasks for writing report<br>


| Task        | Responsible |
| ----------- | ----------- |
| Section 1,2,3 |  Eric Hallberg     |
| Er Diagram|  Eric Hallberg     |
| Section 1,4  |  Samuel Gunnarsson     |
| Component diagram  |  Samuel Gunnarsson     |
| Section 1,5    |  Zhiijie Wei     |
| use case diagram    |  Zhiijie Wei     |



---
----
### Attendencies 
|Team members| 11/8 | 11/10 | 11/15 | 11/17 | 11/22 | 11/24 |  11/29 | 12/1 | 12/6 | 12/8 | 12/10| 12/13 | 12/15 | 12/20| 12/22|12/27| 12/29 | 1/3| 1/5
|---|---| ------ |----|---| ---| ---| ---|---| ---| ---| ---|---| ---|---|--- |--- |--- |---||---|
| Eemil Jeskanen | ✅ |✅| ✅ | ✅| ✅| ✅| ✅| ❌| ❌| ❌| ❌| ❌| ❌|❌|❌|❌|❌|❌|❌|
| Effat Enti| ✅ |✅| ✅| ✅| ✅| ✅|❌ | ✅|❌ | ✅| ✅| ❌| ✅| ❌|❌| ❌|❌|❌|❌|❌|❌|
| Eric Hallberg| ✅ |✅ | ✅ | ✅| ✅ |✅| ✅| ✅| ✅ |✅| ✅| ✅| ✅ |✅| ✅| ✅|✅|✅|✅|
| Samuel Gunnarsson| ✅ |✅| ✅| ✅| ✅ |✅| ✅| ✅|✅ |✅| ✅| ✅|✅ |✅| ✅| ✅|✅| ✅|✅|✅|
| Zhiijie Wei   | ✅ |✅| ✅| ✅| ✅| ✅| ✅| ✅| ✅| ✅| ✅ |✅ | ❌ |✅ | ✅| ✅| ✅|✅|✅|



