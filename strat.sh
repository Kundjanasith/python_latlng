while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "Text read from file: $line"
    python x.py $line
done < "$1"
