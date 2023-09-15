#!/usr/bin/env bash

repo_path=https://github.com/Scouts-Victoria-Program/scouthack_webdev_walkthrough

#for commit in $(git log --reverse --format=%H)
#do
#	short_hash=$(git show --format=%h -s "$commit")
#	subject=$(git show --format=%s -s "$commit")
#	#body=$(git show --format=%b -s "$commit")
#	body=$(git show --format=%B -s "$commit" | sed 1d)
#	diff=$(git diff "$commit"~ "$commit")
#
#	printf '# %s\n[%s](%s/commit/%s)\n\n%s\n\n%s' "$subject" "$short_hash" "$repo_path" "$short_hash" "$body" "$diff"
#done > walkthrough.md

git log -p --reverse --format='```%n%n</details>%n%n# %s%n[%h]('"$repo_path"'/commit/%H)%n%n%b%n%n<details open><summary>diff</summary>%n%n```diff {.numberLines}' |
    sed \
        -e '1,4d;$a```\n\n</details>' \
        -e '/```diff/{N;s/\n//}' > walkthrough.md
sed 's/ {.numberLines}/=/g' walkthrough.md > walkthrough_hedgedoc.md
pandoc -s walkthrough.md -o walkthrough.html
