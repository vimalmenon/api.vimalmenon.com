export type TutorialType = "Tutorial" | "Subject" | "Topic";

export interface IBaseTable {
  uid: string;
  createDate: string;
  updatedDate: string;
}

export interface ITutorial extends IBaseTable {
  title: string;
  description: string;
  type: TutorialType;
}

export interface ISubject extends IBaseTable {
  title: string;
  description: string;
  type: TutorialType;
  tutorialId: string;
}

export interface ITopic extends IBaseTable {
  title: string;
  description: string;
  type: TutorialType;
  content: ITopicContent;
  subjectId: string;
}

export interface ITopicContent {
  code?: string;
  options?: string[];
  description: string[];
  note?: string;
  youtube?: string;
}
