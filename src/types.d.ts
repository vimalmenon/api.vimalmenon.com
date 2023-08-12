export type TutorialType = "Tutorial" | "Subject" | "Topic";
export interface IBaseTable {
  uid: string;
  createDate: string;
  updatedDate: string;
}
export interface ITutorial extends IBaseTable {
  title: string;
  type: TutorialType;
}
export interface ISubject extends IBaseTable {
  title: string;
  type: TutorialType;
}
export interface ITopic extends IBaseTable {
  title: string;
  type: TutorialType;
  content: string;
}
