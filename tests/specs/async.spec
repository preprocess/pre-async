--DESCRIPTION--

Test async macro

--GIVEN--

async function read($path) {
    $content = yield \Amp\File\get($path);
    return $content;
}

$async = async function($path) {
    $content = yield \Amp\File\get($path);
    return $content;
};

--EXPECT--

function read($path)
{
    return call_user_func(function ($context·0) {
        return Amp\call(function () use ($context·0) {
            extract($context·0);

            $content = yield \Amp\File\get($path);
            return $content;
        });
    }, get_defined_vars());
}

$async = call_user_func(function ($outer·1) {
    return function ($path) use ($outer·1) {
        return Amp\call(
                call_user_func(function ($inner·1) use ($outer·1) {
                    return function () use ($outer·1, $inner·1) {
                        extract($outer·1);
                        extract($inner·1);
                        $content = yield \Amp\File\get($path);
                        return $content;
                    };
                }, get_defined_vars())
            );
    };
}, get_defined_vars());
