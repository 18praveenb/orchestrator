#!/usr/bin/env zsh

echo "Removing old files..."
rm -v output/*.html
rm -v temp/*.temp

echo "Compiling links..."
for infile in sources/*.md; do
    infile=$(basename $infile)
    file=${infile%.*}
    outfile=${file}.html
    echo "<a href=\"${outfile}\">${file}</a><br />" >> temp/links.temp
done

cat t0.html temp/links.temp t1.html > temp/template.temp

echo "Generating outputs..."
for infile in sources/*.md; do
    infile=$(basename $infile)
    file=${infile%.*}
    outfile=${file}.html
    pandoc -o output/$outfile sources/$infile --standalone --standalone --mathml --template temp/template.temp --metadata pagetitle=$file -c resources/styles.css
done

echo "Copying resources..."
cp -r resources output

echo "Make complete!"