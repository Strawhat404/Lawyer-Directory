export interface Attorney {
  id: number;
  name: string;
  nickname: string;
  barNumber: string;
  status: string;
  firm: string;
  state: string;
  stateCode: string;
  city: string;
  cityDisplay: string;
  address: string;
  phone: string;
  otherPhones: string;
  email: string;
  description: string;
  slug: string;
}

export interface AttorneysData {
  attorneys: Attorney[];
  metadata: {
    total: number;
    totalRaw: number;
    skipped: number;
    lastUpdated: string;
    cities: string[];
    filesProcessed: number;
  };
}
