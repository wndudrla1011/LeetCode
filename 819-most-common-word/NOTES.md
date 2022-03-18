# 정규 표현식
 * re.sub r -> escape 처리(\만 넣어도 \ 2개 넣은 효과)
 * \w : 문자를 의미
 * ^ : not
 * ref : https://yganalyst.github.io/data_handling/memo_6/#4-%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D-r%EC%9D%98-%EC%9D%98%EB%AF%B8

# Counter 객체
 * List에서 item에 대한 개수를 카운팅
 * return dict
 * ({값:빈도수})
 * collections.Counter(대상)
 * 확장 함수 : most_common(빈도 등수)
 * ex) most_common(1) : 빈도수 1등 반환

# Tip
 * Unification delimeter
 * 여러 문자를 split 하고 싶은 상황
 * 해당 문자들을 replace를 통해 공백으로 만듦
 * 문자열.split()
