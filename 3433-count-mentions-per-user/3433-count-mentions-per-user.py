class Solution(object):
    def countMentions(self, numberOfUsers, events):
        events.sort(key=lambda e: (int(e[1]), e[0] != "OFFLINE"))
        
        mentions = [0] * numberOfUsers
        online_until = [0] * numberOfUsers
        
        for etype, ts, data in events:
            t = int(ts)
            if etype == "OFFLINE":
                uid = int(data)
                online_until[uid] = t + 60
            else:
                if data == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif data == "HERE":
                    for i in range(numberOfUsers):
                        if online_until[i] <= t:
                            mentions[i] += 1
                else:
                    for token in data.split():
                        uid = int(token[2:])
                        mentions[uid] += 1
        return mentions
